import React, { Component } from 'react';
import { decorate, observable, action } from 'mobx';
import { observer } from 'mobx-react';

class Counter extends Component {
    number = 0;

    increase = () => {
        this.number++;
    }

    decrease = () => {
        this.number--;
    }

    render() {
        return (
            <div>
                <h1>{this.number}</h1>
                <button onClick={this.increase}>+1</button>
                <button onClick={this.decrease}>-1</button>
            </div>
        );
    }
}

decorate(Counter, {
    number: observable,
    increase: action,
    decrease: action
})

export default observer(Counter);