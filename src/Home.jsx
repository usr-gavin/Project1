import { BrowserRouter as Router, Route, Link, Routes } from "react-router-dom";



import Login from "./Login";
import Registration from "./Registration";
import PatientList from "./PatientList";


function App() {
  return (
    <div className="App">
      <Router>
        <Routes>
          <Route exact path="/" element={<h1>Home Page</h1>} />
          <Route exact path="Login" element={<Login />} />
          <Route exact path="Registration" element={<Registration />} />
          <Route exact path="PatientList" element={<PatientList />} />
         
        </Routes>
        <div className="list">
          <ul>
            <li><Link to="/">Home</Link></li>
            <li><Link to="Login">Login</Link></li>
            <li><Link to="Registration">Registration</Link></li>
            <li><Link to="PatientList">patientList</Link></li>
            
          </ul>
        </div>
      </Router>
    </div>
  );
}

export default App;