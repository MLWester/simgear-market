import { useEffect, useState } from "react";
import axios from "axios";

export default function HomePage() {
  const [message, setMessage] = useState("");

  useEffect(() => {
    axios.get("/api/test")
      .then((res) => {
        setMessage(res.data.message);
      })
      .catch((err) => {
        console.error("API Error:", err);
        setMessage("❌ Failed to connect to API");
      });
  }, []);

  return (
    <div className="p-4">
      <h1 className="text-2xl font-bold">Home Page</h1>
      <p className="mt-4 text-green-600">{message}</p>
    </div>
  );
}
