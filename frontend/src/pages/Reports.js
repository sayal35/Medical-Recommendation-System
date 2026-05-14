import { useEffect, useState } from "react";

function Reports() {

  const [reports, setReports] = useState([]);
  const [selectedReport, setSelectedReport] = useState(null);

  useEffect(() => {
    const data = JSON.parse(localStorage.getItem("reports")) || [];
    setReports(data);
  }, []);

  return (
    <div className="reportsPage">

      <h1>📊 Reports Summary</h1>

      {reports.length === 0 && (
        <p>No reports generated yet</p>
      )}

      {/* ---------------- LIST ---------------- */}
      {reports.map((r, i) => (
        <div
          className="card clickable"
          key={i}
          onClick={() => setSelectedReport(r)}
          style={{ cursor: "pointer" }}
        >
          <h3>🦠 {r.disease}</h3>
          <p>{r.description?.slice(0, 100)}...</p>

          <small style={{ color: "#94a3b8" }}>
            {r.date}
          </small>
        </div>
      ))}

      {/* ---------------- MODAL ---------------- */}
      {selectedReport && (
        <div className="modalOverlay" onClick={() => setSelectedReport(null)}>

          <div className="modalContent" onClick={(e) => e.stopPropagation()}>

            <h2>🧠 Full Medical Report</h2>

            <h3>🦠 Disease</h3>
            <p>{selectedReport.disease}</p>

            <h3>📖 Description</h3>
            <p>{selectedReport.description}</p>

            <h3>⚠ Precautions</h3>
            <ul>
              {selectedReport.precautions?.map((p, i) => (
                <li key={i}>{p}</li>
              ))}
            </ul>

            <h3>💊 Medications</h3>
            <ul>
              {selectedReport.medications?.map((m, i) => (
                <li key={i}>{m}</li>
              ))}
            </ul>

            <h3>🥗 Diet</h3>
            <ul>
              {selectedReport.diet?.map((d, i) => (
                <li key={i}>{d}</li>
              ))}
            </ul>

            <h3>🏃 Workout</h3>
            <ul>
              {selectedReport.workout?.map((w, i) => (
                <li key={i}>{w}</li>
              ))}
            </ul>

            <button
              onClick={() => setSelectedReport(null)}
              style={{ marginTop: "15px" }}
            >
              Close
            </button>

          </div>

        </div>
      )}

    </div>
  );
}

export default Reports;