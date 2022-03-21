import Vue from 'vue';
import Vuetify from 'vuetify';
import 'vuetify/dist/vuetify.min.css';
import '@mdi/font/css/materialdesignicons.css';
import colors from 'vuetify/lib/util/colors';

Vue.use(Vuetify);

const opts = {
    theme: {
        themes: {
            light: {
                primary: colors.brown.darken1
            }
        }
    }
};

export default new Vuetify(opts);
