import axios from 'axios';

const _apiBaseUrl = 'http://127.0.0.1:5000/';

export const getAllDrinks = async () => {
    const _endpoint = 'get_all_drinks';

    try {
        const response = await axios.get(_apiBaseUrl + _endpoint);

        if (response.status === 200) {
            return response.data
        }
        else {
            return [];
        }

    }
    catch (error) {
        return error.response.data;
    }
};

export const getDetailById = async (id) => {
    const _endpoint = `get_detail_by_id?id=${id}`;

    try {
        const response = await axios.get(_apiBaseUrl + _endpoint);

        if (response.status === 200) {
            return response.data
        }
        else {
            return [];
        }

    }
    catch (error) {
        return error.response.data;
    }
};

export const verifyDoses = async (doseA, doseB) => {
    const _endpoint = `verify-doses?dose_A=${doseA}&dose_B=${doseB}`;

    try {
        const response = await axios.get(_apiBaseUrl + _endpoint);

        return response.data;

    }
    catch (error) {
        return error.response.data;
    }
};

export const prepareDrink = async (doseA, doseB, qtdA, qtdB) => {
    const _endpoint = `make-order?dose_A=${doseA}&dose_B=${doseB}&qtd_A=${qtdA}&qtd_B=${qtdB}`;

    try {
        const response = await axios.post(_apiBaseUrl + _endpoint, null);

        return response;

    }
    catch (error) {
        return error.response;
    }
};

export const updateDrinkLevels = async () => {
    const _endpoint = 'update-level';

    try {
        const response = await axios.put(_apiBaseUrl + _endpoint, null);

        if (response.status === 200) {
            return true;
        }
        else {
            return false;
        }
    }
    catch (error) {
        return false;
    }
};

