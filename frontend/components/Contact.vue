<template>
  <section class="hero">
    <div class="hero-body">
      <div class="container">
        <div class="columns is-vcentered is-centered is-desktop">
          <div class="column if-half">
              <ul>
                  <li v-for="contact in contacts" :key="contact.id">
                      {{ contact.name }}
                  </li>
              </ul>
              <div style="margin-top: 2rem;">
                  <div class="field">
                    <label for="" class="label">Nome</label>
                    <div class="control">
                     <input v-model="name" type="text" class="input" placeholder="Nome do contato">
                    </div>
                  </div>
                  <div class="has-text-right field">
                    <button @click="addContact" class="button is-primary">Cadastrar</button>
                  </div>
              </div>
          </div>
        </div>
      </div>
    </div>
  </section>
</template>

<script>
import Axios from 'axios';

export default {
    name: "Contact",
    data() {
        return {
            contacts: [],
            name: ""
        }
    },
    async mounted() {
        this.contacts = await this.getContacts();
    },
    methods: {
        async getContacts() {
            const res = await Axios({
                url: "/contacts",
                method: "GET"
            });
            return res.data;
        },
        async addContact() {
            const res = await Axios({
                url: "/contacts",
                method: "POST",
                data: {
                    name: this.name
                }
            })

            this.contacts.push({ id: res.data.id, name: res.data.name })
            this.name = ""
        }
    }
};
</script>
