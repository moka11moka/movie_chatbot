import axios from 'axios'
import VueAxios from 'vue-axios'
import Qs from 'qs'
import '../media/styles/style.css'

axios.defaults.xsrfHeaderName = "X-CSRFToken"
axios.defaults.xsrfCookieName = "csrftoken"


var VueCookie = require('vue-cookie')


var new_axios = axios.create({
    transformRequest: [function(data){
        data = Qs.stringify(data);
        return data;
    }],
    headers: {
        "Content-Type": "application/x-www-form-urlencoded",
        "Access-Control-Allow-Origin": "*",
        "Authorization": "Token " + VueCookie.get('accesstoken')
    }
});

Vue.config.delimiters = ["[", "]"];
Vue.use(VueCookie);
Vue.use(VueAxios, new_axios);


var myVue = Vue.extend({
    components: {

    },
    data(){
        return {
            drawer: false,
        }
    }
});

export default myVue


