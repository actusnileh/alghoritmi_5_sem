import { HeaderMenu, Lab3Window } from "../../components";
import { FC, useState } from "react";

export const Lab3Page: FC = () => {
    const [lcsData, setLcsData] = useState<number[][] | null>(null);
    const [directions, setDirectData] = useState<string[][] | null>(null);
    const [all_lcs, setAllLcsData] = useState<string[] | null>(null);

    const handleCalculate = async (input1: string, input2: string) => {
        const queryParams = new URLSearchParams({
            element_1: input1,
            element_2: input2,
        }).toString();

        const response = await fetch(
            `http://localhost:3415/v1/lab3?${queryParams}`,
            {
                method: "GET",
                headers: {
                    Accept: "application/json",
                },
            }
        );
        const result = await response.json();

        setLcsData(result.elements); // таблица LCS
        setDirectData(result.directions); // направления
        setAllLcsData(result.all_lcs); // все возможные LCS
    };

    return (
        <>
            <HeaderMenu />
            <Lab3Window
                onCalculate={handleCalculate}
                lcsData={lcsData}
                directions={directions}
                all_lcs={all_lcs ? all_lcs.join(", ") : ""}
            />
        </>
    );
};
