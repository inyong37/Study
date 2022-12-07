import React, { Component } from 'react';

class App extends Component {
  state = {
    hello: 'hello app js!',
    count: 0
  };

  handleChange = () => {
    this.setState({
      hello: 'bye app js!'
    });
  }

  countUp = () => {
    this.setState({
      count: this.state.count + 1
    });
  }

  countDown = () => {
    this.setState({
      count: this.state.count - 1
    });
  }

  render() {
    return (
      <div className="App">
        <h3>index props</h3>
        <div className="props">
          {/* Props가 들어가는 부분 */}
          <span>{this.props.message}</span>
        </div>

        <h3>state</h3>
        <div className="state">
          {/* State가 들어가는 부분 */}
          <div>{this.state.hello}</div>
          <button onClick={this.handleChange}>click me!</button>
          <div>{this.state.count}</div>
          <button onClick={this.countUp}>+</button>
          <button onClick={this.countDown}>-</button>
        </div>

        <h3>App Props</h3>
        <div className='inside-app-props'>
          <InsideApp
            p1={this.state.count}
            p2={this.countUp}
          />
        </div>
        </* https://berkbach.com/%EA%B8%B0%EC%B4%88%EB%B6%80%ED%84%B0-%EB%B0%B0%EC%9A%B0%EB%8A%94-react-part-6-5bb4b072621a */>
      </div>
    );
  }
}

class InsideApp extends Component {
  render() {
    return (
      <div>
        {this.props.p1}
        <button onClick={this.props.p2}>click me!</button>
      </div>
    );
  };
}

export default App;
