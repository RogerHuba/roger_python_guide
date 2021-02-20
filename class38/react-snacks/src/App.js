import React from 'react';
// import logo from './logo.svg';
import './App.css';

// function App() {
//   return (
//     <div className="App">
//       <header className="App-header">
//         <img src={logo} className="App-logo" alt="logo" />
//         <p>
//           Edit <code>src/App.js</code> and save to reload.
//         </p>
//         <a
//           className="App-link"
//           href="https://reactjs.org"
//           target="_blank"
//           rel="noopener noreferrer"
//         >
//           Learn React
//         </a>
//       </header>
//     </div>
//   );
// }

class App extends React.Component {

 constructor(props) {
      super(props);
      this.state = {
        snacks : [
            {
              id: 1,
              name: 'twix',
              type: 'candy',
            },
            {
              id: 2,
              name: 'snickers',
              type: 'candy'
,            }
        ],
        popularSnack : 'Nothing Yet'
      }
    }

  render() {
    return(
      <div className="App">
        <Header popularSnack={this.state.popularSnack}/>
        <main>
          {/*<SnackList snacks={this.state.snacks}/>*/}
          <SnackList snacks={this.state.snacks} onSnackCreate={(snack) => alert(snack.name)} />
        </main>
        <Footer footerText='This is a Footer'/>
      </div>
    )
  }
}

function Header(props){
  // Lets have this render our the first snack in the list
  return <h2>Popular snack is: {props.popularSnack}</h2>
}

function SnackList(props){
  return (
    <>
      <h2>Snacks</h2>
        <ul>
          {props.snacks.map(snack => <Snack items={snack} key={snack.id} />)}
        </ul>
      {/*{props.onSnackCreate()}*/}
      <SnackForm onSnackCreate={props.onSnackCreate} />
      <button>Create a New Snack</button>
    </>
  )
}

class SnackForm extends React.Component {
  constructor(props) {
    super(props)
    this.state = {
      name: '',
      snackType: '',
    }
    this.handleChange = this.handleChange.bind(this);
    this.handleSubmit = this.handleSubmit.bind(this);
  }

  handleChange(event){
    let newName = event.target.value;
    this.setState({
      name: newName
    })
  }

  handleSubmit(event) {
    event.preventDefault();
    this.props.onSnackCreate(this.state);
  }

  render() {
    // return <h2>this</h2>
  return(
    <form onSubmit={this.handleSubmit}>
      <label>
        Name:
        <input type="text" value={this.state.name} onChange={this.handleChange}/>
      </label>
    </form>
    )
  }

}

function Snack(props) {
  return <li>I am a snack: {props.items.name}</li>
}

function Footer(props) {
  return <footer><small>{props.footerText}</small></footer>
}

export default App;
