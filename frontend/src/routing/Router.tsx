import { createBrowserRouter } from "react-router-dom";
import {
    HomePage,
    Lab2Page,
    Lab3Page,
    Lab4Page,
    Lab5Page,
    Lab6Page,
    Lab7Page,
} from "../pages";

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
    {
        path: "/lab5",
        element: <Lab5Page />,
    },
    {
        path: "/lab6",
        element: <Lab6Page />,
    },
    {
        path: "/lab7",
        element: <Lab7Page />,
    },
]);
