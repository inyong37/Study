// https://velog.io/@velopert/MobX-2-%EB%A6%AC%EC%95%A1%ED%8A%B8-%ED%94%84%EB%A1%9C%EC%A0%9D%ED%8A%B8%EC%97%90%EC%84%9C-MobX-%EC%82%AC%EC%9A%A9%ED%95%98%EA%B8%B0-oejltas52z

import React from 'react';
import ReactDOM from 'react-dom';
import  { Porvider } from 'mobx-react';
import App from './App';
import CounterStore from './stores/counter';

const counter = new CounterStore();

ReactDOM.render(
  <Provider counter={counter}>
    <App />
  </Porivder>
  document.getElementById('root')
);
