# Frontend Next.js TypeScript - Backend Health

Questa app Next.js mostra lo stato del backend effettuando una chiamata a `/health`.

## Avvio locale

```bash
npm install
npm run dev
```

Apri `http://localhost:3000`.

## Build Docker multi-stage

```bash
docker build -t backend-health-frontend .
docker run --rm -p 3000:3000 backend-health-frontend
```

Il container usa una build multi-stage ottimizzata con output `standalone`.
