import axios from 'axios'

export class CookieStand {

    constructor(info) {
        this.id = info.id;
        this.location = info.location;
        this.minCustomersPerHour = info.minimum_customers_per_hour;
        this.maxCustomersPerHour = info.maximum_customers_per_hour;
        this.avgCookiesPerSale = info.average_cookies_per_sale;
        this.cookiesEachHour = info.hourly_sales || [...hours].fill(0);
        this.totalDailyCookies = this.cookiesEachHour.reduce((sum, val) => sum + val);
    }
}

export async function getToken(values) {
    const url = "https://cookie-stand-api.herokuapp.com/api/token/";

    const response = await axios.post(url, values);

    const refreshUrl = "https://cookie-stand-api.herokuapp.com/api/token/refresh";

    const refreshResponse = await axios.post(refreshUrl, { refresh: response.data.refresh });

    return refreshResponse.data.access;
}

export async function fetchWithToken(url, token) {

    let config = {
        headers: {
            'Authorization': 'Bearer ' + token
        }
    }

    const response = await axios.get(url, config);

    const stands = response.data.map(info => new CookieStand(info));

    return stands;
}

export async function postWithToken(url, token, body) {
    let config = {
        headers: {
            'Authorization': 'Bearer ' + token
        }
    }

    const response = await axios.post(url, body, config);

    return response.data;
}
