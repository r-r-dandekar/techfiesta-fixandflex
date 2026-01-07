import React from 'react';
function App() {
  return (
    <div style={{ width: '100vw', height: '100vh', overflow: 'hidden' }}>
      <iframe
        src="/framer-template.html"
        style={{
          width: '100%',
          height: '100%',
          border: 'none',
          display: 'block'
        }}
        title="Framer Template"
        loading="lazy"
      />
    </div>
  );
}

export default App;
