import { useState } from 'react'
import reactLogo from './assets/react.svg'
import './App.css'
import { Button, IconButton, ButtonGroup, ButtonToolbar, Navbar } from 'rsuite';
import NavBar from 'rsuite';

function App() {
  const instance = (
    <ButtonToolbar>
      <Button appearance="default">Default</Button>
    </ButtonToolbar>
  );


  const navbarInstance = (
    <Navbar>
    <Navbar.Brand>
      Hello
    </Navbar.Brand>
    </Navbar>
  )

  return (
    <div className="App">
      {instance}
    </div>
  )
}

export default App
