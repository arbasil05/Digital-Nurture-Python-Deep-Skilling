from fastapi.security.oauth2 import OAuth2PasswordRequestForm
from fastapi.security import OAuth2PasswordBearer
from security import get_password_hash,verify_password,create_access_token,decode_access_token
from fastapi import HTTPException
from sqlalchemy import select
from database import get_db
from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession
from schemas import UserCreate, UserResponse, CourseCreate, CourseResponse
from fastapi import status
import models
from database import engine
from fastapi import FastAPI
from contextlib import asynccontextmanager
from fastapi.middleware.cors import CORSMiddleware

origins = [
    "https://localhost:3000"
]

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/auth/login/")

async def get_current_user(
    token: str = Depends(oauth2_scheme), 
    db: AsyncSession = Depends(get_db)
):
  
    email = decode_access_token(token)
    
    if email is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Could not validate credentials or token expired",
            headers={"WWW-Authenticate": "Bearer"},
        )
        
    query = select(models.User).where(models.User.email == email)
    result = await db.execute(query)
    user = result.scalar_one_or_none()
    
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
        
    return user

@asynccontextmanager
async def lifespan(app:FastAPI):
    async with engine.begin() as conn:
        await conn.run_sync(models.Base.metadata.create_all)
    yield

app = FastAPI(title="FastAPI Auth System",lifespan=lifespan)

app.add_middleware(
    CORSMiddleware,
    allow_origins = origins,
    allow_credentials = True,
    allow_methods = ["*"],
    allow_headers = ["*"],
)

@app.post('/api/auth/register/',response_model=UserResponse,status_code=status.HTTP_201_CREATED,tags=["Authentication"],description="Register new user")
async def register_user(user:UserCreate,db:AsyncSession=Depends(get_db)):
    query = select(models.User).where(models.User.email == user.email)
    result = await db.execute(query)
    existing_user = result.scalar_one_or_none()

    if existing_user:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="Email already registered")
    
    hashed_pw = get_password_hash(user.password)

    db_user = models.User(email=user.email,hashed_password=hashed_pw)
    db.add(db_user)
    await db.commit()
    await db.refresh(db_user)

    return db_user

@app.post('/api/auth/login/',tags=["Authentication"],description="Login")
async def login(form_data:OAuth2PasswordRequestForm = Depends(),db:AsyncSession = Depends(get_db)):
    # OAuth2 forms always use field name but user can type email
    query = select(models.User).where(models.User.email == form_data.username)
    result = await db.execute(query)
    user = result.scalar_one_or_none()

    if not user or not verify_password(form_data.password,user.hashed_password):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Incorrect username or password",headers={"WWW-Authenticate":"Bearer"})
    
    access_token = create_access_token(data={"sub":user.email})

    return {"access_token":access_token,"token_type":"bearer"}

@app.post('/api/courses/', response_model=CourseResponse, status_code=status.HTTP_201_CREATED, tags=['Protected'])
async def create_course(
    course: CourseCreate,
    db: AsyncSession = Depends(get_db),
    current_user: models.User = Depends(get_current_user)
):
    """Create a new course (Protected)"""
    # Check if a course with the same code already exists
    query = select(models.Course).where(models.Course.code == course.code)
    result = await db.execute(query)
    existing_course = result.scalar_one_or_none()
    if existing_course:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Course with this code already exists"
        )
    
    db_course = models.Course(**course.model_dump())
    db.add(db_course)
    await db.commit()
    await db.refresh(db_course)
    return db_course

@app.get('/api/users/me/', tags=['Protected'])
async def read_users_me(current_user: models.User = Depends(get_current_user)):
    return {"email": current_user.email, "id": current_user.id}