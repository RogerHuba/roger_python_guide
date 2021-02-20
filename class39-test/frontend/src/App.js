import React from "react";
import './App.css';
import superagent from "superagent";

class App extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      todo: [],
    };
  }

  handleGetTodo = async () => {
    let url = "http://127.0.0.1:8000/api/v1/todo";
    let results = await superagent.get(url);
    console.log(results);
    let data = results.body;
    console.log(data);
    let todoitem = data.map((item) => [item.title, item.description, item.completed]);
    this.setState({ todo: todoitem })
  }

  render(){
    return(
        <div className="App">
          <Header todoitems={this.state.todo} />
          <button className="Button" onClick={this.handleGetTodo}>
            Click to Load Data
          </button>
          <Todo todo={this.state.todo}/>
        </div>
    )
  }
}

function Header(props) {
  return(
    <h2>You currently have {props.todoitems.length} Todos not Completed!</h2>
  )
}

function Todo(props) {
  return (
    <ul>
      {props.todo.map((title) => (
        <li key={title}> {title}</li>
      ))}
    </ul>
  );
}

export default App;
