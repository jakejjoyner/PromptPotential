import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'

// https://vite.dev/config/
export default defineConfig({
  server: {
        host: '0.0.0.0',
        port: 5173,
        strictPort: true, // if you want Vite to fail if the port is already in use
        cors: {
            origin: 'http://localhost', // or the specific origin of your Laravel app
            credentials: true,
        },
        hmr: {
            host: 'localhost',
        },
    },
  plugins: [react()],
})
