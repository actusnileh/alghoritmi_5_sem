import { HeaderMenu, MainWindow } from "../../components";
import { useState } from "react";
import axios from "axios";
import { SortingResult } from "../../types/lab1_types";

export const HomePage = () => {
    const [loading, setLoading] = useState(false);
    const [sortingResults, setSortingResults] = useState<SortingResult[]>([]);
    const [sortPercent, setSortPercent] = useState<string>("50%");
    const [sortMassive, setSortMassive] = useState<string>("5000");

    const fetchSortingResults = async () => {
        try {
            setLoading(true);
            const response = await axios.get(
                `http://localhost:8000/v1/lab1`,
                { params: { size_massive: parseInt(sortMassive),sort_percent: parseInt(sortPercent) } }
            );
            setSortingResults(response.data.data);
        } catch (error) {
            console.error("Ошибка получения данных с API:", error);
        } finally {
            setLoading(false);
        }
    };

    return (
        <>
            <HeaderMenu />
            <MainWindow
                sortingResults={sortingResults}
                loading={loading}
                sortPercent={sortPercent}
                setSortPercent={setSortPercent}
                sortMassive={sortMassive}
                setSortMassive={setSortMassive}
                fetchSortingResults={fetchSortingResults}
            />
        </>
    );
};
