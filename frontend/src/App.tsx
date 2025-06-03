import {
  BrowserRouter as Router,
  // Routes,
  // Route,
  // Navigate,
  Link,
} from "react-router-dom";

function App() {
  return (
    <Router>
      <nav>
        <Link to="/home">Home</Link>
        <Link to="/departments">Departments</Link>
      </nav>
    </Router>
  );
}

export default App;
