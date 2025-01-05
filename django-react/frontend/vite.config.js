import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'

// https://vite.dev/config/
export default defineConfig({
  base:'/',
  plugins: [react()],
  optimizeDeps: {
    exclude: ['chunk-REFQX4J5'] // Replace with the actual module causing issues
  },

})
