/**
 * Created by liying on 2017/7/27.
 */
import ajax from './ajax'
export  default  {
    register_post (bodyPar) {
        return ajax('POST', '/register', {bodyParams: bodyPar})
    },
    lianlian_get () {
        return ajax('GET', '/lianlian', {})
    }
    // lianlian_post () {
    //     return ajax()
    // }
}
