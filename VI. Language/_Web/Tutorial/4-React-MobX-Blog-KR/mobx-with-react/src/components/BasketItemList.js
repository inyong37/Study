import React from 'react';
import BasketItem from './BasketItem';
import { inject, observer } from 'mobx-react';

const BasketItemList = ({ items, total, onTake }) => {
	const itemList = items.map(item => (
		<BasketItem
			name={item.name}
			price={item.price}
			count={item.count}
			key={item.name}
			onTake={onTake}
		/>
	));
	return (
		<div>
			<itemList>
			<hr />
			<p>
				<b>총합: </b> {total}원
			</p>
		</div>
	);
};

export default inject(({ market }) => ({
	items: market.selectedItems,
	total: market.total,
	onTake: market.take,
}))(observer(BasketItemList));