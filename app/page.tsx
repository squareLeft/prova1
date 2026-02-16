'use client';

import { useEffect, useMemo, useState } from 'react';

type HealthState = 'loading' | 'healthy' | 'unhealthy';

function getStatusColor(state: HealthState): string {
  switch (state) {
    case 'healthy':
      return '#008236';
    case 'unhealthy':
      return '#b91c1c';
    default:
      return '#ca8a04';
  }
}

export default function HomePage() {
  const [state, setState] = useState<HealthState>('loading');
  const [details, setDetails] = useState<string>('Verifica dello stato backend in corso...');

  const statusLabel = useMemo(() => {
    switch (state) {
      case 'healthy':
        return 'Backend online';
      case 'unhealthy':
        return 'Backend non raggiungibile';
      default:
        return 'Controllo in corso';
    }
  }, [state]);

  const checkHealth = async () => {
    setState('loading');
    setDetails('Chiamata a /health in corso...');

    try {
      const response = await fetch('/health', { cache: 'no-store' });
      const body = await response.text();

      if (response.ok) {
        setState('healthy');
        setDetails(body || 'OK');
      } else {
        setState('unhealthy');
        setDetails(`HTTP ${response.status}${body ? ` - ${body}` : ''}`);
      }
    } catch (error) {
      setState('unhealthy');
      const message = error instanceof Error ? error.message : 'Errore sconosciuto';
      setDetails(message);
    }
  };

  useEffect(() => {
    checkHealth();
  }, []);

  return (
    <main className="container">
      <section className="card" aria-live="polite">
        <h1>Stato backend</h1>

        <p className="status" style={{ color: getStatusColor(state) }}>
          ● {statusLabel}
        </p>

        <p className="details">Dettagli: {details}</p>

        <button type="button" onClick={checkHealth}>
          Aggiorna stato
        </button>
      </section>
    </main>
  );
}
