import React from 'react';
import {Link} from "react-router-dom";

const Nav = (props: { name: string, setName: (name: string) => void }) => {
    const logout = async () => {
        await fetch('http://localhost:8000/log/logout', {
            method: 'POST',
            headers: {'Content-Type': 'application/json'},
            credentials: 'include',
        });

        props.setName('');
    }

    let menu;
    
     console.log(props.name)
     
    if (props.name === '' || props.name===undefined) {
        menu = (
            <ul className="navbar-nav me-auto mb-2 mb-md-0">
                <li className="nav-item active">
                    <Link to="/" className="nav-link">Login</Link>
                </li>
                <li className="nav-item active">
                    <Link to="/register" className="nav-link">Register</Link>
                </li>
                
            </ul>
        )
    } 
    
    else {
        menu = (
            <ul className="navbar-nav me-auto mb-2 mb-md-0">
                <li className="nav-item active">
                    <Link to="/" className="nav-link" onClick={logout}>Logout</Link>
                </li>
            </ul>
        )
    }

    return (
        <nav className="navbar navbar-expand-md navbar-dark bg-dark mb-4">
            <div className="container-fluid">
                <Link to="/home" className="navbar-brand">Ai-SMRFT</Link>

                <div>
                    {menu}
                </div>
            </div>
        </nav>
    );
};

export default Nav;
