export interface SortingResult {
    name: string;
    massive: number;
    time: number;
}

export interface MainWindowProps {
    sortingResults: SortingResult[];
    loading: boolean;
    sortPercent: string;
    setSortPercent: React.Dispatch<React.SetStateAction<string>>;
    sortMassive: string;
    setSortMassive: React.Dispatch<React.SetStateAction<string>>;
    fetchSortingResults: () => void;
}

export interface Lab2WindowProps {
    onValuesChange?: (values: string) => void;
    onCalculate: () => void;
    matrixData?: {
        matrix: number[][];
        k: number[][];
        optimal_brackets: string;
    };
}
