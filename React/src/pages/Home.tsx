import React,{useEffect, useState} from 'react';

const Home = (props: { name: string }) => {

    const[pname,setPname]=useState('');

    useEffect(() => {
        (
            async () => {
                const response2 = await fetch('http://localhost:8000/log/patient' , {
                    headers: {'Content-Type': 'application/json'},
                    credentials: 'include',
                });
                const contentp=await response2.json();
                
                setPname(contentp.PatientName)
            }
        )();
    });
    
    return (
        <div>
            {props.name ? 'Hi ' + props.name : 'You are not logged in'}<br></br>
            PatientName:{pname}
            

            
        </div>
    );
};

export default Home;