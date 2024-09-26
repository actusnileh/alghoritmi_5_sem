import { HeaderMenu, Lab3Window } from "../../components";
import { FC, useState } from "react";

export const Lab3Page: FC = () => {
    const [lcsData, setLcsData] = useState<number[][] | null>(null);

    const handleCalculate = async (input1: string, input2: string) => {
        const queryParams = new URLSearchParams({
            element_1: input1,
            element_2: input2,
        }).toString();

        const response = await fetch(
            `http://0.0.0.0:8000/v1/lab3?${queryParams}`,
            {
                method: "GET",
                headers: {
                    Accept: "application/json",
                },
            }
        );

        const result = await response.json();
        setLcsData(result.data);
    };

    return (
        <>
            <HeaderMenu />
            <Lab3Window onCalculate={handleCalculate} lcsData={lcsData} />
        </>
    );
};
