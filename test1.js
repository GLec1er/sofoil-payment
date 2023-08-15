function printOrderTotal(responseString) {
    try {
        const responseJSON = JSON.parse(responseString);
        let orderSubtotal = 0;

        responseJSON.forEach(function(item) {
            if (item.price === undefined) {
                item.price = 0;
            }
            orderSubtotal += item.price;
        });

        const total = orderSubtotal;

        console.log('Стоимость заказа: ' + (total > 0 ? total + ' руб.' : 'Бесплатно'));
    } catch (error) {
        console.error('Ошибка при обработке данных:', error);
    }
}


