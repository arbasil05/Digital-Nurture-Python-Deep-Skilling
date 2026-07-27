# Hands-on 10: API Integration & Advanced State Management

This directory contains the React implementation for Hands-on 10, demonstrating a centralized API service layer, advanced Redux Toolkit async thunks, and global error handling via Error Boundaries.

## State Management Framework Comparison

As part of this hands-on, here is a brief comparison of how the three major frameworks handle state management:

### 1. React + Redux (Redux Toolkit)
- **Concept:** Uses a strict unidirectional data flow (Actions -> Reducers -> Store -> Selectors -> Components).
- **Boilerplate:** Historically very high, but Redux Toolkit (RTK) significantly reduced boilerplate by providing `createSlice`, `createAsyncThunk`, and built-in Immer for immutable updates.
- **Learning Curve:** Moderate to High. Concepts like immutability, thunks for async logic, and selectors take time to master.
- **Built-in Tooling:** Redux DevTools is the gold standard for time-travel debugging.

### 2. Angular + NgRx
- **Concept:** Deeply integrates Redux patterns with RxJS (Observables). State changes happen via Actions and Reducers, but side effects (like API calls) are handled entirely separately by "Effects".
- **Boilerplate:** Very High. Requires defining Actions, Reducers, Selectors, and Effects in separate files (though `createActionGroup` in newer versions helps).
- **Learning Curve:** High. Developers must understand both Redux patterns and RxJS streams/operators thoroughly.
- **Built-in Tooling:** Excellent integration with Angular's dependency injection and strong typing via TypeScript.

### 3. Vue + Pinia
- **Concept:** Replaced Vuex as the official state management tool for Vue. It provides a Store that directly exposes state, getters, and actions.
- **Boilerplate:** Very Low. You define stores almost exactly like standard Vue Composition API setup functions (using `ref`, `computed`, and standard `async/await` functions).
- **Learning Curve:** Low. It feels like writing normal Vue components. No dispatching actions or writing complex reducers.
- **Built-in Tooling:** Fantastic integration with Vue DevTools. It also simplifies reactivity (e.g., using `storeToRefs` allows destructuring state while maintaining reactivity without complex selectors).
