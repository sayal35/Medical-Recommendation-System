function Footer() {
  return (
    <div className="footer">
      <p>© {new Date().getFullYear()} MedAI System | Built for Medical Assistance</p>
      <p className="small">⚠ This system is AI-based and not a substitute for a doctor</p>
    </div>
  );
}

export default Footer;