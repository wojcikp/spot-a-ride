<template>
  <div>
    <upper-bar />
    <main-menu />

    <v-form class="mt-10 pt-10">
      <v-container>
        <v-card class="pa-6">
          <v-row>
            <v-col
              cols="6"
            >
              <v-select
                :items="brands"
                v-model="brand"
                label="Marka:"
                required
              ></v-select>
            </v-col>
            <v-col
              cols="6"
            >
              <v-text-field
                v-model="model"
                label="Model:"
                hint="Podaj nazwę modelu identyczną jak na otomoto"
              ></v-text-field>
            </v-col>
          </v-row>
          <v-row>
            <v-col
              cols="6"
            >
              <v-text-field
                v-model="productionYearFrom"
                label="Rok produkcji od:"
              ></v-text-field>
            </v-col>
            <v-col
              cols="6"
            >
              <v-text-field
                v-model="productionYearTo"
                label="Rok produkcji do:"
              ></v-text-field>
            </v-col>
          </v-row>
          <v-row>
            <v-col
              cols="6"
            >
              <v-text-field
                v-model="mileageLimit"
                label="Przebieg do:"
              ></v-text-field>
            </v-col>
            <v-col
              cols="6"
            >
              <v-text-field
                v-model="priceLimit"
                label="Cena do:"
              ></v-text-field>
            </v-col>
          </v-row>
          <v-row>
            <v-col>
              <v-btn @click="addOffer" :disabled="this.brand === null" color="teal darken-1" class="mr-3 white--text">Dodaj</v-btn>
              <v-btn class="ml-3" @click="clearForm">Wyczyść</v-btn>
            </v-col>
          </v-row>
        </v-card>
      </v-container>
    </v-form>
  </div>
</template>

<script>
import { mapActions } from 'vuex'
import MainMenu from './MainMenu.vue'
import UpperBar from './UpperBar.vue'

export default {
  components: { MainMenu, UpperBar },
  name: 'NewSearchForm',

  data () {
    return {
      brand: null,
      model: null,
      productionYearFrom: null,
      productionYearTo: null,
      mileageLimit: null,
      priceLimit: null,
      brands: [
        'Abarth', 'Acura', 'Aiways', 'Aixam', 'Alfa Romeo', 'Alpine', 'Asia', 'Aston Martin', 'Audi', 'Austin', 'Autobianchi',
        'Baic', 'Bentley', 'BMW', 'BMW-ALPINA', 'Brilliance', 'Bugatti', 'Buick', 'BYD', 'Cadillac', 'Casalini', 'Caterham',
        'Cenntro', 'Changan', 'Chatenet', 'Chevrolet', 'Chrysler', 'Citroën', 'Cupra', 'Dacia', 'Daewoo', 'Daihatsu', 'DeLorean',
        'DFSK', 'DKW', 'Dodge', 'DR MOTOR', 'DS Automobiles', 'FAW', 'Ferrari', 'Fiat', 'Ford', 'Gaz', 'Geely', 'Genesis',
        'GMC', 'GWM', 'Honda', 'Hongqi', 'Hummer', 'Hyundai', 'iamelectric', 'Ineos', 'Infiniti', 'Inny', 'Isuzu',
        'Iveco', 'Jaguar', 'Jeep', 'Jetour', 'Kia', 'KTM', 'Lada', 'Lamborghini', 'Lancia', 'Land Rover', 'LEVC', 'Lexus',
        'Ligier', 'Lincoln', 'Lotus', 'LTI', 'Lucid', 'Lynk & Co', 'MAN', 'Maserati', 'Maxus', 'Maybach', 'Mazda', 'McLaren',
        'Mercedes-Benz', 'Mercury', 'MG', 'Microcar', 'MINI', 'Mitsubishi', 'NIO', 'Nissan', 'Nysa', 'Oldsmobile', 'Opel', 'Peugeot',
        'Piaggio', 'Plymouth', 'Polestar', 'Polonez', 'Pontiac', 'Porsche', 'RAM', 'Renault', 'Rolls-Royce', 'Rover', 'Saab', 'Seat',
        'Seres', 'Shuanghuan', 'Skoda', 'Skywell', 'Smart', 'SsangYong', 'Subaru', 'Suzuki', 'Syrena', 'Tarpan', 'Tata', 'Tesla',
        'Toyota', 'Trabant', 'Triumph', 'Uaz', 'Vauxhall', 'VELEX', 'Volkswagen', 'Volvo', 'Warszawa', 'Wartburg', 'Wołga', 'XPeng',
        'Zaporożec', 'Zastava', 'ZEEKR', 'Żuk']
    }
  },

  methods: {
    ...mapActions([
      'addSearchedOffer'
    ]),
    addOffer () {
      this.addSearchedOffer({
        brand: this.brand,
        model: this.model,
        productionYearFrom: this.productionYearFrom,
        productionYearTo: this.productionYearTo,
        mileageLimit: this.mileageLimit,
        priceLimit: this.priceLimit
      })
    },
    clearForm () {
      this.brand = null
      this.model = null
      this.productionYearFrom = null
      this.productionYearTo = null
      this.mileageLimit = null
      this.priceLimit = null
    }
  }
}
</script>
