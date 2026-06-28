import { useEffect, useState } from "react";
import api from "../api/api";

function Dashboard() {
  const [cities, setCities] = useState([]);

  useEffect(() => {
    async function fetchCities() {
      try {
        const response = await api.get("/cities");
        console.log(response.data);

        setCities(response.data);
      } catch (error) {
        console.error("Error loading cities:", error);
      }
    }

    fetchCities();
  }, []);

  return (
    <div className="flex-1 p-8">
      <h2 className="text-3xl font-bold text-white mb-8">
        Dashboard
      </h2>

      <div className="rounded-xl bg-slate-800 p-8">
        <h3 className="text-xl font-semibold text-cyan-400 mb-4">
          Cities
        </h3>

        <ul className="space-y-2">
          {cities.map((city) => (
            <li
              key={city.id}
              className="text-slate-300"
            >
              {city.city_name} ({city.state})
            </li>
          ))}
        </ul>
      </div>
    </div>
  );
}

export default Dashboard;