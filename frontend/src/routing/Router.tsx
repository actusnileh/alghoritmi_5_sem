import { createBrowserRouter } from "react-router-dom";
import { HomePage, Lab2Page, Lab3Page, Lab4Page } from "../pages";

export const router = createBrowserRouter([
    {
        path: "/",
        element: <HomePage />,
    },
    {
        path: "/lab2",
        element: <Lab2Page />,
    },
    {
        path: "/lab3",
        element: <Lab3Page />,
    },
    {
        path: "/lab4",
        element: <Lab4Page />,
    },
]);
