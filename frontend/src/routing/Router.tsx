import { createBrowserRouter } from "react-router-dom";
import { HomePage, Lab2Page } from "../pages";

export const router = createBrowserRouter([
    {
        path: "/",
        element: <HomePage />,
    },
    {
        path: "/lab2",
        element: <Lab2Page />,
    },
]);
