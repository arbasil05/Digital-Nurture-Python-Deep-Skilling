import { Component, OnInit } from '@angular/core';
import { FormsModule } from '@angular/forms';
import { CourseCard } from '../course-card/course-card';
import { Course } from '../course';

@Component({
  selector: 'app-course-list',
  imports: [CourseCard, FormsModule],
  templateUrl: './course-list.html',
  styleUrl: './course-list.css',
})
export class CourseList implements OnInit {

  searchTerm: string = "";
  courses: any[] = [];
  isLoading: boolean = true;

  constructor(private course: Course) { }

  ngOnInit() {
    this.isLoading = true;

    this.course.getCourses().subscribe({
      next: (data) => {
        this.courses = data.map((item: any) => ({
          name: item.title.substring(0, 20) + '...',
          code: `CS${item.id * 100}`,
          credits: 3,
          grade: 'Pending'
        }));
        this.isLoading = false;
      },
      error: (err) => {
        console.error('Failed to fetch courses', err);
        this.isLoading = false;
      }
    });
  }

  get filteredCourses() {
    return this.courses.filter(course => course.name.toLowerCase().includes(this.searchTerm.toLowerCase()));
  }

}
