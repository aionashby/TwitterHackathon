import React, { Component } from "react";
import logo from "./logo.svg";
import "./App.css";
import flappy from "./flappy.gif";
import fire from "./fire.gif";
import audioWave from "./audiowaves.gif";
import ChatBubble from "./ChatBubble.js";
import content from "./content.json";

class App extends Component {
  state = {
    messages: [
      {
        type: 0,
        image: fire,
        text: "Hey Twitter!"
      },
      {
        type: 1,
        image: flappy,
        text: "Hey! I'm listening!"
      }
    ]

    // messages: contentList.map(
    //   message => {
    //     type: message.type;
    //   },
    //   { image: message.image },
    //   { text: message.text }
    // )
  };

  handleNewMessage = text =>
    this.setState({
      messages: this.state.messages.concat([
        {
          text,
          type: 0,
          image: fire
        }
      ])
    });

  render() {
    return (
      <div className="App">
        <header className="App-header">
          <h2>Hey Twitter!</h2>
        </header>
        <div className="body-container">
          <div className="text-container">
            {/* <img src={logo} className="App-logo" alt="logo" />

            <p>
              Edit <code>src/App.js</code> and save to reload.
            </p>
            <a
              className="App-link"
              href="https://reactjs.org"
              target="_blank"
              rel="noopener noreferrer"
            >
              Hey Twitter
            </a>
            <div className="Audio-image">
              <img src={audioWave} alt="loading..." />
            </div>
            <h2>Aion!!</h2> */}
            <ChatBubble
              messages={this.state.messages}
              onNewMessage={this.handleNewMessage}
            />
          </div>
        </div>
      </div>
    );
  }
}

export default App;
