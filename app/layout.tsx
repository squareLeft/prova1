import type { Metadata } from 'next';
import './globals.css';

export const metadata: Metadata = {
  title: 'Backend Health Monitor',
  description: 'Frontend Next.js che monitora /health del backend',
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang="it">
      <body>{children}</body>
    </html>
  );
}
