import { useEffect, useState } from "react";
import Select from "react-select";
import "../App.css"

function Home() {

  const [options, setOptions] = useState([]);
  const [selectedSymptoms, setSelectedSymptoms] = useState([]);
  const [report, setReport] = useState(null);
  const [loading, setLoading] = useState(false);

  const customStyles = {
    control: (base) => ({
      ...base,
      backgroundColor: "#111827",
      borderColor: "#374151",
      color: "white"
    }),
    menu: (base) => ({
      ...base,
      backgroundColor: "#111827"
    }),
    option: (base, state) => ({
      ...base,
      backgroundColor: state.isFocused ? "#1f2937" : "#111827",
      color: "white"
    }),
    singleValue: (base) => ({
      ...base,
      color: "white"
    })
  };

  useEffect(() => {
    fetch("http://127.0.0.1:5000/symptoms")
      .then(res => res.json())
      .then(data => {
        const formatted = data.map(s => ({
          label: s.replace(/_/g, " "),
          value: s
        }));
        setOptions(formatted);
      });
  }, []);

 const predict = async () => {

  if (selectedSymptoms.length === 0) {
    alert("Please select at least one symptom");
    return;
  }

  setLoading(true);

  const response = await fetch("http://127.0.0.1:5000/predict", {
    method: "POST",
    headers: {
      "Content-Type": "application/json"
    },
    body: JSON.stringify({
      symptoms: selectedSymptoms.map(s => s.value).join(" ")
    })
  });

  const data = await response.json();

  setLoading(false);

  if (!data.success) {
    alert(data.message || data.error);
    return;
  }
  setReport(data);

  // 🔥 SAVE TO LOCAL STORAGE (IMPORTANT FIX)
  const oldReports = JSON.parse(localStorage.getItem("reports")) || [];

  const updatedReports = [
    {
      ...data,
      date: new Date().toLocaleString()
    },
    ...oldReports
  ];

  localStorage.setItem("reports", JSON.stringify(updatedReports));
};

  return (
    <div className="layout">

      {/* LEFT PANEL */}
      <div className="leftPanel">

        <h1>🧠 MedAI System</h1>
        <p className="subtitle">AI Disease Prediction System</p>

        {/* SYMPTOM SELECT */}
        <Select
          options={options}
          isMulti
          onChange={setSelectedSymptoms}
          placeholder="Select symptoms..."
          className="dropdown"
          styles={customStyles}   
        />

        <button onClick={predict}>
          Generate Report
        </button>

        {loading && <p className="loading">Analyzing symptoms...</p>}

      </div>

      {/* RIGHT PANEL */}
      <div className="rightPanel">

        {!report && !loading && (
          <div className="emptyState">
            <h2>📋 No Report Generated</h2>
            <p>Select symptoms and generate medical report</p>
          </div>
        )}

        {report && (
          <div className="report">

            {/* HEADER */}
            <div className="headerCard">
              <h2>Medical Report</h2>
            </div>

            {/* DISEASE */}
            <div className="card highlight">
              <h3>🦠 Disease</h3>
              <p>{report.disease}</p>
            </div>

            {/* DESCRIPTION */}
            <div className="card">
              <h3>📖 Description</h3>
              <p>{report.description}</p>
            </div>

            {/* GRID SECTION */}
            <div className="grid">

              <div className="card">
                <h3>⚠ Precautions</h3>
                <ul>
                  {report.precautions?.map((item, i) => (
                    <li key={i}>{item}</li>
                  ))}
                </ul>
              </div>

              <div className="card">
                <h3>💊 Medications</h3>
                <ul>
                  {report.medications?.map((item, i) => (
                    <li key={i}>{item}</li>
                  ))}
                </ul>
              </div>

              <div className="card">
                <h3>🥗 Diet</h3>
                <ul>
                  {report.diet?.map((item, i) => (
                    <li key={i}>{item}</li>
                  ))}
                </ul>
              </div>

              <div className="card">
                <h3>🏃 Workout</h3>
                <ul>
                  {report.workout?.map((item, i) => (
                    <li key={i}>{item}</li>
                  ))}
                </ul>
              </div>

            </div>

          </div>
        )}

      </div>

    </div>
  );
}

export default Home;