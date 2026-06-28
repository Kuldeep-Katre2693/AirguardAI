import Navbar from "./components/Navbar";
import Sidebar from "./components/Sidebar";
import Footer from "./components/Footer";
import Dashboard from "./pages/Dashboard";

function App() {
  return (
    <div className="min-h-screen bg-slate-900">

      <Navbar />

      <div className="flex">

        <Sidebar />

        <Dashboard />

      </div>

      <Footer />

    </div>
  );
}

export default App;