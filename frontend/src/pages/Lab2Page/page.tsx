import axios from "axios";
import { HeaderMenu, Lab2Window } from "../../components";
import { FC, useState } from "react";

export const Lab2Page: FC = () => {
    const [values, setValues] = useState<string>("");

    const handleValuesChange = (newValues: string) => {
        setValues(newValues);
    };

    const fetchMatrixResult = async () => {
        try {
            const response = await axios.get(`http://localhost:8000/v1/lab2`, {
                params: {
                    p: values,
                },
            });
            console.log("Matrix result:", response.data);
        } catch (error) {
            console.error("Ошибка получения данных с API:", error);
        }
    };

    return (
        <>
            <HeaderMenu />
            <Lab2Window onValuesChange={handleValuesChange} />
        </>
    );
};
