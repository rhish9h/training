# Module 8: Frontend with React - Learning Resources (Part 2)

## 8.3 React Router & API

### 8.3.1 - React Router

#### Core Concepts
- Single Page Application (SPA) routing
- React Router v6 implementation
- Route parameters and nested routes
- Protected routes and authentication
- Navigation guards and redirects
- Code splitting with lazy loading

#### Search Terms
- "React Router v6 tutorial TypeScript"
- "SPA routing best practices React"
- "Nested routes React Router examples"
- "Protected routes authentication React"
- "Navigation guards React Router"
- "Code splitting React Router lazy loading"

#### Suggested Learning Path
1. **Router Fundamentals** (1 hour)
   - Understand SPA routing
   - Learn React Router setup
   - Explore route configuration

2. **Route Parameters** (1 hour)
   - Implement dynamic routes
   - Create parameter extraction
   - Design route matching

3. **Nested Routes** (1 hour)
   - Create route hierarchy
   - Implement outlet components
   - Design layouts with nested routes

4. **Protected Routing** (1 hour)
   - Implement authentication checks
   - Create route guards
   - Design redirect logic

5. **Code Splitting** (1 hour)
   - Implement lazy loading
   - Create suspense boundaries
   - Design chunking strategy

#### Recommended Resources

**Official Documentation**
- [React Router Documentation](https://reactrouter.com/en/main)
- [React Router with TypeScript](https://reactrouter.com/en/main/guides/typescript)
- [React Lazy Loading](https://react.dev/reference/react/lazy)

**Articles & Tutorials**
- [React Router v6 Complete Guide](https://blog.logrocket.com/react-router-v6-guide/)
- [Protected Routes with React Router](https://medium.com/@dennisivy/creating-protected-routes-with-react-router-v6-2c7114b55ecd)
- [Code Splitting in React](https://www.digitalocean.com/community/tutorials/react-code-splitting-libraries)

**YouTube Videos**
- [React Router v6 Tutorial (Net Ninja)](https://www.youtube.com/watch?v=xNaQWkOTMwg)
- [Protected Routes (Web Dev Simplified)](https://www.youtube.com/watch?v=Mcr1t6mxOWk)
- [React Router Code Splitting (Jack Herrington)](https://www.youtube.com/watch?v=YwbwTI5jVmQ)

**GitHub Repositories**
- [react-router-examples](https://github.com/remix-run/react-router/tree/main/examples)
- [protected-routes-example](https://github.com/bforbis/react-router-protected-routes)
- [code-splitting-example](https://github.com/facebook/react/tree/main/fixtures/code-splitting)

---

### 8.3.2 - API Integration

#### Core Concepts
- React API integration patterns
- Fetch API and Axios comparison
- Custom hooks for API requests
- Error handling and loading states
- Request caching and optimization
- Authentication token management

#### Search Terms
- "React API integration best practices"
- "Fetch vs Axios React comparison"
- "Custom hooks for API requests React"
- "API error handling patterns React"
- "Request caching React applications"
- "Authentication token management React"

#### Suggested Learning Path
1. **API Fundamentals** (1 hour)
   - Compare API clients
   - Understand REST principles
   - Explore request/response patterns

2. **Client Setup** (1 hour)
   - Configure API client
   - Create request interceptors
   - Design response handling

3. **Custom Hooks** (1 hour)
   - Implement reusable request hooks
   - Create loading/error states
   - Design hook composition

4. **Error Handling** (1 hour)
   - Implement global error handling
   - Create retry mechanisms
   - Design user feedback

5. **Authentication Flow** (1 hour)
   - Implement token management
   - Create refresh strategies
   - Design secure storage

#### Recommended Resources

**Official Documentation**
- [Fetch API](https://developer.mozilla.org/en-US/docs/Web/API/Fetch_API)
- [Axios Documentation](https://axios-http.com/docs/intro)
- [React Query](https://tanstack.com/query/latest)

**Articles & Tutorials**
- [API Integration in React](https://www.robinwieruch.de/react-hooks-fetch-data/)
- [Custom Hooks for API Calls](https://kentcdodds.com/blog/replace-axios-with-a-simple-custom-fetch-wrapper)
- [Authentication Flow in React](https://blog.logrocket.com/jwt-authentication-with-react-typescript/)

**YouTube Videos**
- [React API Integration (Web Dev Simplified)](https://www.youtube.com/watch?v=xHbA7i8QCl8)
- [Custom Hooks for API Calls (Jack Herrington)](https://www.youtube.com/watch?v=sB9pv-NVVws)
- [Auth Token Management (Traversy Media)](https://www.youtube.com/watch?v=nI8PYZNFtac)

**GitHub Repositories**
- [react-query-examples](https://github.com/tanstack/query/tree/main/examples/react)
- [api-hooks-example](https://github.com/alan2207/bulletproof-react/tree/master/src/lib/hooks)
- [auth-token-management](https://github.com/cornflourblue/react-hooks-axios-jwt-auth)

---

### 8.3.3 - Mocking & Testing APIs

#### Core Concepts
- API mocking strategies for development
- MSW (Mock Service Worker) implementation
- Testing API integrations
- Handling API dependencies in tests
- Snapshot testing for API responses
- Integration testing with API interactions

#### Search Terms
- "Mock Service Worker (MSW) React tutorial"
- "API mocking strategies React development"
- "Testing API integrations React"
- "Snapshot testing API responses"
- "React Testing Library API mocking"
- "Integration testing API interactions React"

#### Suggested Learning Path
1. **Mocking Fundamentals** (1 hour)
   - Understand API mocking concepts
   - Learn different mocking approaches
   - Explore testing requirements

2. **MSW Setup** (1 hour)
   - Configure Mock Service Worker
   - Create request handlers
   - Design mock responses

3. **Unit Testing** (1 hour)
   - Implement component tests with mocks
   - Create API hook testing
   - Design snapshot testing

4. **Integration Testing** (1 hour)
   - Implement multi-component tests
   - Create user flow testing
   - Design realistic scenarios

5. **CI/CD Integration** (1 hour)
   - Configure testing in pipelines
   - Create environment-specific mocks
   - Design test reporting

#### Recommended Resources

**Official Documentation**
- [Mock Service Worker](https://mswjs.io/)
- [React Testing Library](https://testing-library.com/docs/react-testing-library/intro/)
- [Jest Documentation](https://jestjs.io/docs/getting-started)

**Articles & Tutorials**
- [API Mocking with MSW](https://kentcdodds.com/blog/stop-mocking-fetch)
- [Testing API Integrations in React](https://www.robinwieruch.de/react-testing-library/)
- [Snapshot Testing for API Responses](https://jestjs.io/docs/snapshot-testing)

**YouTube Videos**
- [MSW Tutorial (Jack Herrington)](https://www.youtube.com/watch?v=Ofw12_s1zAY)
- [Testing API Calls (Web Dev Simplified)](https://www.youtube.com/watch?v=04BBgg8zgWY)
- [React Testing Library (Net Ninja)](https://www.youtube.com/watch?v=7dTTFW7yACQ)

**GitHub Repositories**
- [msw-examples](https://github.com/mswjs/examples)
- [testing-library-examples](https://github.com/kentcdodds/react-testing-library-examples)
- [api-testing-patterns](https://github.com/alan2207/bulletproof-react/tree/master/src/test)

---

### Branch Project 8.3: Product Catalog

#### Core Concepts
- Full-featured product catalog application
- React Router with parameter-based navigation
- API integration with search and filtering
- Infinite scrolling and pagination
- Product detail pages and related items
- Cart system with persistent state

#### Search Terms
- "React product catalog application tutorial"
- "Infinite scrolling React implementation"
- "E-commerce filtering and search React"
- "Product detail page React Router"
- "Shopping cart persistent state React"
- "React e-commerce application architecture"

#### Suggested Learning Path
1. **App Architecture** (1-2 hours)
   - Design comprehensive structure
   - Plan routes and navigation
   - Create data flow approach

2. **Product Listing** (1-2 hours)
   - Implement infinite scrolling
   - Create filtering system
   - Design search functionality

3. **Product Details** (1-2 hours)
   - Create detailed product view
   - Implement related products
   - Design specification display

4. **Cart Implementation** (1-2 hours)
   - Create persistent cart state
   - Implement add/remove items
   - Design quantity controls

5. **API Integration** (1-2 hours)
   - Implement comprehensive API client
   - Create request caching
   - Design error handling

#### Recommended Resources

**Official Documentation**
- [React Router](https://reactrouter.com/en/main)
- [React Query](https://tanstack.com/query/latest)
- [Redux Toolkit](https://redux-toolkit.js.org/)

**Articles & Tutorials**
- [Building an E-commerce Site with React](https://medium.com/siliconwat/building-an-e-commerce-site-with-react-using-context-api-and-hooks-6e51bbe6c647)
- [Infinite Scrolling in React](https://www.smashingmagazine.com/2020/03/infinite-scroll-lazy-image-loading-react/)
- [Shopping Cart Implementation](https://blog.logrocket.com/building-a-full-featured-shopping-cart-in-react/)

**YouTube Videos**
- [E-commerce React Tutorial (Coding With Basir)](https://www.youtube.com/watch?v=N4uVHgmQWTY)
- [Infinite Scroll Implementation (Web Dev Simplified)](https://www.youtube.com/watch?v=NZKUirTtxcg)
- [Shopping Cart in React (Traversy Media)](https://www.youtube.com/watch?v=nKyrXWH5XLM)

**GitHub Repositories**
- [react-shopping-cart](https://github.com/jeffersonRibeiro/react-shopping-cart)
- [react-ecommerce](https://github.com/adrianhajdin/project_e_commerce)
- [product-catalog-example](https://github.com/basir/amazona)

## 8.4 Testing & Performance

### 8.4.1 - React Testing

#### Core Concepts
- Modern React testing approach
- React Testing Library fundamentals
- Component testing strategies
- Mock implementations for dependencies
- User event simulation
- Test-driven development in React

#### Search Terms
- "React Testing Library tutorial TypeScript"
- "Component testing strategies React"
- "Mock implementations React testing"
- "User event simulation testing React"
- "Test-driven development React example"
- "Testing React hooks and context"

#### Suggested Learning Path
1. **Testing Fundamentals** (1 hour)
   - Understand React testing approaches
   - Learn testing principles
   - Explore testing library setup

2. **Component Tests** (1 hour)
   - Implement rendering tests
   - Create interaction testing
   - Design snapshot tests

3. **Mock Dependencies** (1 hour)
   - Create mock implementations
   - Implement context mocking
   - Design service substitution

4. **User Interactions** (1 hour)
   - Implement event simulation
   - Create form submission tests
   - Design complex interactions

5. **TDD Approach** (1 hour)
   - Implement test-first development
   - Create feature specifications
   - Design test-driven workflow

#### Recommended Resources

**Official Documentation**
- [React Testing Library](https://testing-library.com/docs/react-testing-library/intro/)
- [Jest Documentation](https://jestjs.io/docs/getting-started)
- [User Event Library](https://testing-library.com/docs/user-event/intro/)

**Articles & Tutorials**
- [Complete Guide to React Testing](https://www.freecodecamp.org/news/testing-react-hooks/)
- [Testing React Components](https://kentcdodds.com/blog/common-mistakes-with-react-testing-library)
- [Test-Driven Development in React](https://www.smashingmagazine.com/2020/07/react-apps-testing-library/)

**YouTube Videos**
- [React Testing Library Tutorial (Net Ninja)](https://www.youtube.com/watch?v=7dTTFW7yACQ)
- [TDD in React (Kent C. Dodds)](https://www.youtube.com/watch?v=kCR3JAR7CHE)
- [Testing Hooks and Context (Jack Herrington)](https://www.youtube.com/watch?v=MbUe4Tz1eUg)

**GitHub Repositories**
- [testing-library-examples](https://github.com/kentcdodds/react-testing-library-examples)
- [react-tdd-example](https://github.com/kentcdodds/react-tdd-example)
- [testing-hooks-example](https://github.com/alan2207/bulletproof-react/tree/master/src/test)

---

### 8.4.2 - Performance Optimization

#### Core Concepts
- React component optimization techniques
- Memo, useMemo, and useCallback usage
- React Profiler for performance analysis
- Bundle size optimization strategies
- Code splitting and lazy loading
- Virtual list and windowing techniques

#### Search Terms
- "React performance optimization techniques"
- "useMemo and useCallback optimization patterns"
- "React Profiler performance analysis"
- "Bundle size optimization React"
- "Code splitting and lazy loading React"
- "Virtual list implementation React"

#### Suggested Learning Path
1. **Performance Fundamentals** (1 hour)
   - Understand React rendering
   - Learn optimization principles
   - Explore performance metrics

2. **Memoization Techniques** (1 hour)
   - Implement React.memo
   - Create useMemo optimizations
   - Design useCallback patterns

3. **Profiling & Analysis** (1 hour)
   - Use React Profiler
   - Create performance measurements
   - Design benchmark tests

4. **Bundle Optimization** (1 hour)
   - Implement code splitting
   - Create lazy loading
   - Design dynamic imports

5. **Rendering Optimization** (1 hour)
   - Implement virtual lists
   - Create windowing techniques
   - Design render batching

#### Recommended Resources

**Official Documentation**
- [React Performance Optimization](https://react.dev/reference/react/memo)
- [React Profiler API](https://react.dev/reference/react/Profiler)
- [Code Splitting in React](https://react.dev/reference/react/lazy)

**Articles & Tutorials**
- [Complete Guide to React Performance](https://kentcdodds.com/blog/usememo-and-usecallback)
- [Bundle Size Optimization](https://www.debugbear.com/blog/react-bundle-size-optimization)
- [Virtual Lists in React](https://developers.google.com/web/updates/2016/07/infinite-scroller)

**YouTube Videos**
- [React Performance (Web Dev Simplified)](https://www.youtube.com/watch?v=i9TS9FnmHkI)
- [useMemo and useCallback Deep Dive (Jack Herrington)](https://www.youtube.com/watch?v=_oXuZ8ISlr0)
- [React Profiler Tutorial (Konstantin Münster)](https://www.youtube.com/watch?v=VuzWn-2T_F0)

**GitHub Repositories**
- [react-window](https://github.com/bvaughn/react-window) - Virtualized list library
- [performance-examples](https://github.com/paulirish/automated-chrome-profiling)
- [react-virtualized](https://github.com/bvaughn/react-virtualized)

---

### 8.4.3 - End-to-End Testing

#### Core Concepts
- End-to-end testing with Cypress
- Test scenarios and user flows
- API mocking in E2E tests
- CI/CD pipeline integration
- Visual regression testing
- Test reporting and visualization

#### Search Terms
- "Cypress end-to-end testing React tutorial"
- "Test scenarios and user flows Cypress"
- "API mocking in Cypress tests"
- "CI/CD integration Cypress React"
- "Visual regression testing React applications"
- "Cypress test reporting and visualization"

#### Suggested Learning Path
1. **Cypress Fundamentals** (1 hour)
   - Understand E2E testing concepts
   - Learn Cypress architecture
   - Explore test setup

2. **Test Scenarios** (1 hour)
   - Create user flow tests
   - Implement assertion patterns
   - Design realistic scenarios

3. **API Mocking** (1 hour)
   - Implement request interception
   - Create mock responses
   - Design stub patterns

4. **CI/CD Integration** (1 hour)
   - Configure pipeline integration
   - Create test parallelization
   - Design artifact collection

5. **Visual Testing** (1 hour)
   - Implement snapshot comparison
   - Create visual regression tests
   - Design visual testing workflow

#### Recommended Resources

**Official Documentation**
- [Cypress Documentation](https://docs.cypress.io/)
- [Cypress Testing React](https://docs.cypress.io/guides/component-testing/react/overview)
- [Cypress Visual Testing](https://docs.cypress.io/guides/tooling/visual-testing)

**Articles & Tutorials**
- [E2E Testing with Cypress](https://www.sitepoint.com/react-end-to-end-testing-cypress/)
- [API Mocking in Cypress](https://www.cypress.io/blog/2019/01/22/network-requests/)
- [Visual Regression Testing](https://docs.cypress.io/guides/tooling/visual-testing)

**YouTube Videos**
- [Cypress Tutorial (Net Ninja)](https://www.youtube.com/watch?v=xqwZxG9MqEU)
- [E2E Testing React (Traversy Media)](https://www.youtube.com/watch?v=7N63cMKosIE)
- [Cypress in CI/CD (Cypress.io)](https://www.youtube.com/watch?v=saYovXS9Llk)

**GitHub Repositories**
- [cypress-example-recipes](https://github.com/cypress-io/cypress-example-recipes)
- [cypress-react-examples](https://github.com/cypress-io/cypress-realworld-app)
- [visual-testing-examples](https://github.com/cypress-io/cypress-realworld-app/tree/develop/cypress/tests)

---

### Branch Project 8.4: Perfomance Analyzer

#### Core Concepts
- Performance analysis dashboard
- Component render profiling
- Bundle size visualization
- Lighthouse integration
- Performance regression testing
- Optimization recommendations

#### Search Terms
- "React performance analysis dashboard"
- "Component render profiling implementation"
- "Bundle size visualization React"
- "Lighthouse integration React applications"
- "Performance regression testing framework"
- "React performance optimization recommendations"

#### Suggested Learning Path
1. **Dashboard Architecture** (1-2 hours)
   - Design metrics collection
   - Plan visualization approach
   - Create component structure

2. **Profiling Implementation** (1-2 hours)
   - Implement render timing
   - Create component tracing
   - Design performance reporting

3. **Bundle Analysis** (1-2 hours)
   - Implement webpack analysis
   - Create size visualization
   - Design impact assessment

4. **Lighthouse Integration** (1-2 hours)
   - Set up automated audits
   - Create scoring visualization
   - Design recommendation system

5. **Regression Testing** (1-2 hours)
   - Implement benchmark storage
   - Create comparison analysis
   - Design alerting system

#### Recommended Resources

**Official Documentation**
- [React Profiler API](https://react.dev/reference/react/Profiler)
- [Webpack Bundle Analyzer](https://github.com/webpack-contrib/webpack-bundle-analyzer)
- [Lighthouse CI](https://github.com/GoogleChrome/lighthouse-ci)

**Articles & Tutorials**
- [Building a Performance Dashboard](https://medium.com/netflix-techblog/building-a-high-performance-front-end-for-the-netflix-signup-flow-86de0be1ca74)
- [React Performance Monitoring](https://kentcdodds.com/blog/profile-a-react-app-for-performance)
- [Lighthouse Integration Guide](https://www.smashingmagazine.com/2020/05/lighthouse-performance-budgets/)

**YouTube Videos**
- [React Performance Analysis (Jack Herrington)](https://www.youtube.com/watch?v=y_6U8JyasoQ)
- [Bundle Size Optimization (Ben Awad)](https://www.youtube.com/watch?v=CNuI8OWsppg)
- [Lighthouse CI Tutorial (Google Chrome Developers)](https://www.youtube.com/watch?v=aQcRK3WDGsM)

**GitHub Repositories**
- [webpack-bundle-analyzer](https://github.com/webpack-contrib/webpack-bundle-analyzer)
- [lighthouse-ci](https://github.com/GoogleChrome/lighthouse-ci)
- [react-performance-testing](https://github.com/keiya01/react-performance-testing)

## Module 8 Capstone: Social Media Frontend

#### Core Concepts
- Comprehensive social media application frontend
- Advanced component architecture
- Complex state management
- Real-time updates with WebSockets
- Optimized performance with virtualization
- Comprehensive testing strategy

#### Search Terms
- "Social media application React architecture"
- "Advanced component architecture React"
- "Complex state management social application"
- "Real-time updates WebSockets React"
- "Virtualization techniques social feed"
- "Comprehensive testing strategy React"

#### Suggested Learning Path
1. **Application Architecture** (2-3 hours)
   - Design comprehensive structure
   - Plan component hierarchy
   - Create state management strategy

2. **Core Features** (2-3 hours)
   - Implement feed and posts
   - Create user profiles
   - Design interaction components

3. **Real-time Integration** (2-3 hours)
   - Implement WebSocket connection
   - Create real-time updates
   - Design notification system

4. **Performance Optimization** (2-3 hours)
   - Implement feed virtualization
   - Create lazy loading
   - Design optimized rendering

5. **Testing Implementation** (2-3 hours)
   - Create unit test coverage
   - Implement E2E testing
   - Design visual regression tests

#### Recommended Resources

**Official Documentation**
- [React Advanced Patterns](https://react.dev/learn/escape-hatches)
- [Socket.io Client](https://socket.io/docs/v4/client-api/)
- [React Query](https://tanstack.com/query/latest)

**Articles & Tutorials**
- [Building a Social Media App](https://www.sitepoint.com/build-social-network-app-react-graphql/)
- [Real-time Updates with Socket.io](https://blog.logrocket.com/websockets-tutorial-how-to-go-real-time-with-node-and-react-8e4693fbf843/)
- [Feed Virtualization Techniques](https://blog.logrocket.com/virtualizing-react-rendering-for-improved-performance/)

**YouTube Videos**
- [Social Media App Tutorial (Lama Dev)](https://www.youtube.com/watch?v=zM93yZ_8SvE)
- [WebSockets with React (Traversy Media)](https://www.youtube.com/watch?v=jD7FnbI76Hg)
- [React Performance Optimization (Jack Herrington)](https://www.youtube.com/watch?v=U9e7VkZepF4)

**GitHub Repositories**
- [social-media-app](https://github.com/safak/youtube/tree/mern-social-app)
- [react-social-network](https://github.com/red-gold/react-social-network)
- [react-twitter-clone](https://github.com/EliasAfara/Twitter-Clone)
