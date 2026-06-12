import React, { useEffect, useState } from 'react';
import Map from 'react-map-gl';
import 'mapbox-gl/dist/mapbox-gl.css';

function MapView({ latitude, longitude, geojson }) {
  const [viewState, setViewState] = useState({
    longitude: longitude || -74.006,
    latitude: latitude || 40.7128,
    zoom: 15
  });

  const mapboxToken = process.env.REACT_APP_MAPBOX_TOKEN || 'pk.eyJ1IjoiZXhhbXBsZSIsImEiOiJja2x0eG5vbnEwMXVrMm9wYnZ6b3R5aW5vIn0.example';

  useEffect(() => {
    if (latitude && longitude) {
      setViewState({
        longitude,
        latitude,
        zoom: 15
      });
    }
  }, [latitude, longitude]);

  if (!latitude || !longitude) {
    return (
      <div className="bg-slate-800/50 backdrop-blur-lg rounded-2xl border border-slate-700 p-8 flex items-center justify-center h-96">
        <p className="text-slate-400">Map will appear after geocoding</p>
      </div>
    );
  }

  return (
    <div className="bg-slate-800/50 backdrop-blur-lg rounded-2xl border border-slate-700 overflow-hidden">
      <div className="p-6 border-b border-slate-700">
        <h2 className="text-2xl font-bold text-white">Property Location</h2>
        <p className="text-slate-400 text-sm mt-1">
          {latitude.toFixed(6)}, {longitude.toFixed(6)}
        </p>
      </div>
      <div className="h-96">
        <Map
          {...viewState}
          onMove={evt => setViewState(evt.viewState)}
          style={{ width: '100%', height: '100%' }}
          mapStyle="mapbox://styles/mapbox/streets-v12"
          mapboxAccessToken={mapboxToken}
        >
          {/* Marker for property location */}
          <div
            style={{
              position: 'absolute',
              left: '50%',
              top: '50%',
              transform: 'translate(-50%, -50%)',
              pointerEvents: 'none'
            }}
          >
            <div className="bg-emerald-500 w-4 h-4 rounded-full border-2 border-white shadow-lg" />
          </div>
        </Map>
      </div>
      <div className="p-4 bg-slate-700/30">
        <p className="text-sm text-slate-400 text-center">
          Property boundary shown approximately. Verify with official survey.
        </p>
      </div>
    </div>
  );
}

export default MapView;
