
import { useState } from 'react';



export default function PatientList() {
  const [PatientId, setPatientId] = useState("");

    
  const fetchData = () => {
    console.log("hi")
    fetch('http://localhost:8000/log/patient')
      .then((response) => response.json())
      .then((response) => {
        setPatientId(response);
                console.log(PatientId)
      })
      .catch(() => {
        setPatientId("ERROR");
      });
  };
  return (
    
    <div className="App">
      <center><button onClick={fetchData}>PatientList</button></center>
      
      { PatientId && PatientId.map((patient) => (
        <div key={patient.PatientId}>
          

         <table border="1" align="center">
              <thead>
                <tr>
                  <th>PatientId</th>
                  <th>PatientName</th>
                  <th>Diagnosis</th>
                  <th>consult_Doctor</th>
                  <th>PatientImage</th>
                   </tr>
                </thead>   
                <tbody>
                  
                <tr>
              <td>{patient.PatientId}</td>
              <td>{patient.PatientName}</td>
              <td>{patient.Diagnosis}</td>
              <td>{patient.Con_Doc}</td>
              <td><img src="{patient.PatientImg}" alt="" width="400" height="400" ></img></td>
              </tr>
              
         </tbody>
          </table>
         
        </div>
      ))
      }
     
    </div>

  );
}
