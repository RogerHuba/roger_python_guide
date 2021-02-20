import React from "react";
import "./App.css";

function getSomewhere() {
  return "Texas";
}

function Header(props) {
  return (
    <header>
      <p>Hi in the header</p>
      <p>Props says ... {props.message2}</p>
    </header>
  );
}

function Footer(props) {
  return (
    <footer>
      <p>Hi in the footer</p>
      <p>Props says ... {props.message}</p>
    </footer>
  );
}


export default function App() {
  let userName = "Roger";
  return (
    <>
      <Header message2="I'm in the header" />
      <div className="App">
        <h1>
          Hello CodeSandbox from {userName} in {getSomewhere()}
        </h1>
        <h2>Start editing to see some magic happen!</h2>
      </div>
      <div>
        <h2>hola</h2>
      </div>
      <SectionOne mood={'Happy'}/>
      <Footer message="Hello there General Kenobi" />
      <Footer message="General Kenobi, you scum..." />
    </>
  );
}

class SectionOne extends React.Component {

  constructor() {
    super();
    this.state = {
      mood: 'sad',
    }
  }

  changeMood(change) {
    console.log("change", change);
    // DO NOT DO THIS
    // this.state.mood = 'Happy'
    this.setState({
        mood: 'Happy',
      }
    )
  }


  render() {
    return (
      <>
        <button onClick={() => this.changeMood('imporove')}>Improve</button>
        <button onClick={() => this.changeMood('reduce')}>Reduce</button>
        <h3>Today is a {this.state.mood} Day</h3>
      </>
    )
  }
  // let mood = 'Happy'
  //
}
