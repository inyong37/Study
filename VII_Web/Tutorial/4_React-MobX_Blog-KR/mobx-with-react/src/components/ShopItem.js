import React from 'react';
import './ShopItem.css';

const ShopItem = ({ name, price }) => {
	return (
		<div className="ShopItem" onClick={() => onPut(name, price)}>
			<h4>{name}</h4>
			<div>{price}원</div>
		</div>
	);
};

export default ShopItem;