const btns = ".+123-456/789*(0)"

const Key = {
    props: ['value'],
    template: `<button type = 'button' class = 'btn'>{{value}}</button>`
}

const app = Vue.createApp({
    data(){
        return {
            keys: btns,
            exp: '',
            K: '<'
        }
    },
    methods: {
        Sbros(){
            this.exp = ''
        },
        Dl(){
            this.exp = this.exp.slice(0, -1)
        },
        async calc(e){
            e.preventDefault();
            const input = document.getElementById('input');
            const response = await fetch('/api/calc/', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json;charset=utf-8'
                },
                body: JSON.stringify({expression: input.value})
            });
            const result = await response.json();
            input.placeholder = result.placeholder;
            this.exp = result.value;
        }
    },
    components: {
      Key
    },
})
app.mount('#calc')
