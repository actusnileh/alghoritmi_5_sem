import axios from "axios";
import { HeaderMenu, Lab2Window } from "../../components";
import { FC, useState } from "react";

export const Lab2Page: FC = () => {
    const [values, setValues] = useState<string>("");
    const [matrixData, setMatrixData] = useState<any>(null);

    const handleValuesChange = (newValues: string) => {
        setValues(newValues);
    };

    const fetchMatrixResult = async () => {
        try {
            const response = await axios.get(`http://37.128.205.70:3415/v1/lab2`, {
                params: {
                    p: values,
                },
            });
            console.log("Matrix result:", response.data);
            setMatrixData(response.data);
        } catch (error) {
            console.error("Ошибка получения данных с API:", error);
        }
    };

    return (
        <>
            <HeaderMenu />
            <Lab2Window
                onValuesChange={handleValuesChange}
                onCalculate={fetchMatrixResult}
                matrixData={matrixData}
            />
        </>
    );
};
