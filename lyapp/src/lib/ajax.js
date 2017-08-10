import axios from 'axios';

/**
 * 发送网络请求
 * @param method  HTTP Status
 * @param url     URL
 * @param bodyParams HTTP Body
 * @params UrlParams  URL Params
 * @return {AxiosPromise}
 * **/

export default function (method, url, {bodyParams = {}, urlParams = {}}) {
    //是否存在Access Token，存在则写入HTTP头
    let headers = {};
    // let address = "https://cashier.lianlianpay.com/payment/bankgateway.htm";
    let address = "http://127.0.0.1:5000";
    try {
        let accessToken = sessionStorage.getItem('AccessToken');
        let userID = sessionStorage.getItem('UserID');
        if (accessToken && userID) {
            headers["AccessToken"] = accessToken;
            headers["UserID"] = userID;
        }
    } catch (e){}

    //将url参数写入url
    let  urlParamsStr = '';
    for (let urlParamsKey in urlParams){
        urlParamsStr += `${urlParamsKey}=${urlParams[urlParamsKey]}&`;
    }
    if (urlParamsStr.length !== 0){
        urlParamsStr = `?${urlParamsStr}`.slice(0,-1);

    }
    return axios.request({
        url:`${address}${url}${urlParamsStr}`,
        method,
        headers,
        data:bodyParams
    });
}