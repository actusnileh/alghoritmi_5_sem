import base64

from fastapi import (
    APIRouter,
    Query,
)

from src.schema.backpack_schema import (
    ElementsWithWeight,
    MethodSchema,
)
from src.services.backpack_service import (
    continuous_backpack,
    discrete_backpack,
    Item,
    visualize_continuous_backpack,
    visualize_discrete_backpack,
)


router = APIRouter(tags=["Лаб.Работа №4"], prefix="/lab4")


@router.post("")
async def get_backpack(
    elements_with_weight: ElementsWithWeight,
    capacity: int = Query(
        description="Размер рюкзака",
        ge=1,
    ),
    method: MethodSchema = Query(
        description="Метод",
    ),
):
    items = [
        Item(weight=element.weight, value=element.value)
        for element in elements_with_weight.elements
    ]

    if method == MethodSchema.Continuous:
        total_value, weight_used, result_df = continuous_backpack(items, capacity)
        buf = visualize_continuous_backpack(
            items,
            capacity,
            total_value,
            weight_used,
            result_df["Доля взятая"].tolist(),
        )

        img_base64 = base64.b64encode(buf.getvalue()).decode("utf-8")
        table_html = result_df.to_html(index=False)

        return {
            "max_value": total_value,
            "visualization": f"data:image/png;base64,{img_base64}",
            "table": table_html,
            "text_result": "",
        }

    elif method == MethodSchema.Discrete:
        df, max_value, items_taken_info, text_result = discrete_backpack(
            items,
            capacity,
        )
        buf = visualize_discrete_backpack(df)

        img_base64 = base64.b64encode(buf.getvalue()).decode("utf-8")
        table_html = items_taken_info.to_html(index=False)

        return {
            "max_value": max_value,
            "visualization": f"data:image/png;base64,{img_base64}",
            "table": table_html,
            "text_result": text_result,
        }
