import { createStore } from 'vuex'

import SlaeStore from './modules/SlaeStore'
import DeterminantStore from './modules/DeterminantStore'
import InverseStore from './modules/InverseStore'
import MatrixStore from './modules/MatrixStore'

export default createStore({
  modules: {
    slae: SlaeStore,
    matrix: MatrixStore,
    determinant: DeterminantStore,
    inverse: InverseStore
  }
})
