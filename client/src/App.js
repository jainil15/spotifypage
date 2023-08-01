import logo from "./logo.svg";
import "./App.css";
import { createBrowserRouter, RouterProvider } from "react-router-dom";
import { Top50 } from "./Pages/Top50";
import axios from "axios";
import "./styles.scss";
import { Single } from "./Pages/Single";

axios.defaults.baseURL = "http://localhost:8800";

const router = createBrowserRouter([
  {
    path: "/top50",
    element: <Top50 />,
  },
  {
    path: "/",
    element: <Top50 />,
  },
  {
    path: '/track/:id',
    element: <Single />
  }
]);
function App() {
  return <RouterProvider router={router} />;
}

export default App;
