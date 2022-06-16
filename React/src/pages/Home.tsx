import React,{useEffect, useState} from 'react';

const Home = (props: { name: string }) => {

    var dat=[];
    

    useEffect(() => {
        (
            async () => {
                const response = await fetch('http://localhost:8000/log/patient' , {
                    headers: {'Content-Type': 'application/json'},
                    credentials: 'include',
                });

              
                const pat = await response.json();

                  dat=pat;

                  
                  
                  console.log(dat)

                  
            }
        )();
    });

    
    
    return (
        <div>
            {props.name ? 'Hi ' + props.name : 'You are not logged in'}<br></br>
            
        

        </div>
    );
};

export default Home;